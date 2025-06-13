#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
잠언 전서 크롤링 스크립트
NOCR.net에서 개역개정 잠언 1-31장을 모두 수집하여 TXT 파일로 저장

사용법:
    python proverbs_crawler.py
    python proverbs_crawler.py --output custom_filename.txt
    python proverbs_crawler.py --delay 2.0 --output proverbs.txt
"""

import requests
from bs4 import BeautifulSoup
import time
import re
import argparse
import sys
from datetime import datetime
from urllib.parse import urljoin


class ProverbsCrawler:
    """잠언 크롤러 클래스 - Python/Django 기반 고성능 웹 스크래핑"""
    
    def __init__(self, delay=1.0, verbose=True):
        self.base_url = "https://nocr.net"
        self.delay = delay
        self.verbose = verbose
        
        # 고성능 세션 설정
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
            'Accept-Encoding': 'gzip, deflate, br',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        
        # 타임아웃 설정
        self.session.timeout = 15
        
        # 재시도 설정
        self.max_retries = 3
        
    def log(self, message, level="INFO"):
        """로깅 함수"""
        if self.verbose:
            timestamp = datetime.now().strftime("%H:%M:%S")
            print(f"[{timestamp}] {level}: {message}")
    
    def generate_proverbs_urls(self):
        """잠언 1-31장의 URL 목록 생성"""
        urls = []
        base_id = 4221  # 잠언 1장의 document ID
        
        # URL 패턴 분석: 4221(1장), 4223(2장), 4225(3장)... 
        # 패턴: base_id + (chapter - 1) * 2
        for chapter in range(1, 32):
            document_id = base_id + (chapter - 1) * 2
            url = f"{self.base_url}/korkrv/{document_id}"
            urls.append((chapter, url, document_id))
            
        return urls
    
    def extract_verse_text(self, html_content, chapter):
        """HTML에서 잠언 구절 텍스트 추출"""
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # 다양한 방법으로 본문 텍스트 추출 시도
            content_text = self._extract_content_by_selectors(soup)
            
            if not content_text:
                # 전체 텍스트에서 추출
                content_text = soup.get_text()
            
            # 잠언 구절 패턴 추출
            verses = self._parse_verses(content_text, chapter)
            
            return verses
            
        except Exception as e:
            self.log(f"잠언 {chapter}장 텍스트 추출 오류: {e}", "ERROR")
            return None
    
    def _extract_content_by_selectors(self, soup):
        """CSS 선택자를 사용한 컨텐츠 추출"""
        selectors = [
            '.xe_content',
            '.document_content', 
            '.content',
            'article',
            '.post-content',
            '#content',
            '.entry-content',
            'main',
            '.main-content'
        ]
        
        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                return element.get_text(separator='\n', strip=True)
        
        return None
    
    def _parse_verses(self, text, chapter):
        """텍스트에서 잠언 구절 파싱"""
        lines = text.split('\n')
        verses = []
        
        # 잠언 구절 패턴 (예: "1:1", "1:2" 등)
        verse_pattern = re.compile(rf'^{chapter}:\d+\s+(.+)')
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
                
            # 잠언 구절 패턴 매칭
            match = verse_pattern.match(line)
            if match:
                verses.append(line)
                continue
                
            # 대안 패턴 (구절 번호만 있는 경우)
            if re.match(r'^\d+:\d+\s+', line):
                # 해당 장의 구절인지 확인
                verse_num = line.split(':')[0]
                if verse_num == str(chapter):
                    verses.append(line)
        
        # 중복 제거 및 정렬
        unique_verses = []
        seen = set()
        
        for verse in verses:
            # 구절 번호 추출
            verse_match = re.match(r'^(\d+:\d+)', verse)
            if verse_match:
                verse_key = verse_match.group(1)
                if verse_key not in seen:
                    seen.add(verse_key)
                    unique_verses.append(verse)
        
        # 구절 번호로 정렬
        def get_verse_number(verse):
            match = re.match(r'^(\d+):(\d+)', verse)
            if match:
                return (int(match.group(1)), int(match.group(2)))
            return (0, 0)
        
        unique_verses.sort(key=get_verse_number)
        
        return unique_verses
    
    def fetch_chapter(self, chapter, url, document_id):
        """특정 장의 데이터 가져오기"""
        for attempt in range(self.max_retries):
            try:
                self.log(f"잠언 {chapter}장 요청 중... (시도 {attempt + 1}/{self.max_retries})")
                
                response = self.session.get(url)
                response.raise_for_status()
                response.encoding = 'utf-8'
                
                verses = self.extract_verse_text(response.text, chapter)
                
                if verses and len(verses) > 0:
                    self.log(f"잠언 {chapter}장 수집 완료 ({len(verses)}개 구절)")
                    return verses
                else:
                    self.log(f"잠언 {chapter}장에서 구절을 찾을 수 없음", "WARNING")
                    
                    # 대체 URL 시도
                    if attempt < self.max_retries - 1:
                        alt_document_id = document_id + 1  # 다음 ID 시도
                        alt_url = f"{self.base_url}/korkrv/{alt_document_id}"
                        self.log(f"대체 URL 시도: {alt_url}")
                        url = alt_url
                        continue
                    
                    return None
                    
            except requests.RequestException as e:
                self.log(f"잠언 {chapter}장 요청 실패 (시도 {attempt + 1}): {e}", "ERROR")
                if attempt < self.max_retries - 1:
                    time.sleep(self.delay * (attempt + 1))  # 백오프
                    continue
                else:
                    return None
            except Exception as e:
                self.log(f"잠언 {chapter}장 처리 중 예외 발생: {e}", "ERROR")
                return None
        
        return None
    
    def crawl_all_proverbs(self):
        """모든 잠언 크롤링"""
        self.log("잠언 전체 크롤링 시작 (1-31장)")
        
        urls = self.generate_proverbs_urls()
        all_proverbs = {}
        success_count = 0
        
        for chapter, url, document_id in urls:
            verses = self.fetch_chapter(chapter, url, document_id)
            
            if verses:
                all_proverbs[chapter] = verses
                success_count += 1
            else:
                self.log(f"잠언 {chapter}장 수집 실패", "ERROR")
            
            # 서버 부하 방지
            if chapter < 31:  # 마지막 장이 아닌 경우만
                time.sleep(self.delay)
        
        self.log(f"크롤링 완료: {success_count}/31개 장 수집 성공")
        return all_proverbs
    
    def format_output(self, proverbs_data):
        """출력 형식 생성"""
        content = []
        
        # 헤더
        content.append("개역개정 잠언 전서")
        content.append("=" * 60)
        content.append("")
        content.append("출처: HANGL NOCR (https://nocr.net)")
        content.append("번역: 개역개정판")
        content.append(f"수집일시: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        content.append(f"수집된 장수: {len(proverbs_data)}/31장")
        content.append("")
        content.append("=" * 60)
        content.append("")
        
        # 각 장 데이터
        for chapter in sorted(proverbs_data.keys()):
            verses = proverbs_data[chapter]
            
            content.append(f"=== 잠언 {chapter}장 ===")
            content.append("")
            
            for verse in verses:
                content.append(verse)
            
            content.append("")
            content.append("─" * 50)
            content.append("")
        
        # 푸터
        content.append("")
        content.append("=" * 60)
        content.append("수집 완료")
        content.append("")
        content.append("주의사항:")
        content.append("- 이 데이터는 NOCR.net에서 수집되었습니다")
        content.append("- 모든 저작권은 원저작자에게 있습니다")
        content.append("- 개인 연구 및 학습 목적으로만 사용하세요")
        content.append("")
        
        return '\n'.join(content)
    
    def save_to_file(self, content, filename):
        """파일 저장"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            
            self.log(f"파일 저장 완료: {filename}")
            self.log(f"파일 크기: {len(content.encode('utf-8'))} bytes")
            
        except Exception as e:
            self.log(f"파일 저장 실패: {e}", "ERROR")
            raise


def main():
    """메인 함수"""
    parser = argparse.ArgumentParser(
        description="NOCR.net에서 개역개정 잠언 1-31장 크롤링",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
사용 예시:
    python proverbs_crawler.py
    python proverbs_crawler.py --output my_proverbs.txt
    python proverbs_crawler.py --delay 2.0 --quiet
        """
    )
    
    parser.add_argument(
        '--output', '-o',
        default='개역개정_잠언_전서.txt',
        help='출력 파일명 (기본값: 개역개정_잠언_전서.txt)'
    )
    
    parser.add_argument(
        '--delay', '-d',
        type=float,
        default=1.0,
        help='요청 간 대기 시간(초) (기본값: 1.0)'
    )
    
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='조용한 모드 (로그 출력 안함)'
    )
    
    parser.add_argument(
        '--retries', '-r',
        type=int,
        default=3,
        help='최대 재시도 횟수 (기본값: 3)'
    )
    
    args = parser.parse_args()
    
    # 크롤러 초기화
    crawler = ProverbsCrawler(
        delay=args.delay,
        verbose=not args.quiet
    )
    crawler.max_retries = args.retries
    
    try:
        # 크롤링 실행
        proverbs_data = crawler.crawl_all_proverbs()
        
        if not proverbs_data:
            crawler.log("수집된 데이터가 없습니다.", "ERROR")
            sys.exit(1)
        
        # 출력 형식 생성
        content = crawler.format_output(proverbs_data)
        
        # 파일 저장
        crawler.save_to_file(content, args.output)
        
        # 결과 요약
        if not args.quiet:
            print("\n" + "=" * 60)
            print("크롤링 작업 완료!")
            print(f"수집된 장수: {len(proverbs_data)}/31장")
            print(f"출력 파일: {args.output}")
            print(f"파일 크기: {len(content.encode('utf-8'))} bytes")
            print("=" * 60)
        
    except KeyboardInterrupt:
        crawler.log("사용자에 의해 중단되었습니다.", "INFO")
        sys.exit(0)
    except Exception as e:
        crawler.log(f"예상치 못한 오류 발생: {e}", "ERROR")
        sys.exit(1)


if __name__ == "__main__":
    main()