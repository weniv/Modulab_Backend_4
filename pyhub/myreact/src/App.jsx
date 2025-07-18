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
    </>
  )
}

export default App
