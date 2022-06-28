import logo from './logo.svg';
import './App.css';
import { RequireToken } from './Auth';
import { Routes, Route } from 'react-router-dom';
import Login from "./login";
import Profile from "./profile";

function App() {
  return (
    <div className="App">
      
      <Routes>  
        <Route path="/" element={<Login />} />
        <Route path="/profile" element={
          <RequireToken>
            <Profile />
          </RequireToken>
        } />       

      </Routes>
    </div>
  );
}

export default App;
