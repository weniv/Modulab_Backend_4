import { loadProfile } from './api';
import { useEffect } from 'react'

// App 컴포넌트
function App() {
  // React Hooks
  useEffect(() => {
    console.log("mounted");
    loadProfile();
  }, []);

  return (
    <>
      <h1>Vite + React</h1>

      {/* 미인증 상황에서만 노출 */}
      <a href="http://localhost:8000/accounts/login/?next=http://localhost:5173">로그인</a>
    </>
  )
}

export default App
