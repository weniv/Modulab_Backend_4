import pytest

# pytest는 기본적으로 DB접근을 막고 있어요.

@pytest.mark.django_db
def test_blog_index(client):  # pytest에서 fixture
    # 아래 테스트는 View 단에서 DB접근이 발생합니다.
    res = client.get("/blog/")
    assert res.status_code == 200
