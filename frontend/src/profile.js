import { useNavigate } from "react-router-dom";


export default function Profile() {
    const navigate = useNavigate();

    const signOut = () => {
        localStorage.removeItem("token");
        navigate("/");
    }
    return (
      <>
        <div style={{ marginTop:20, minHeight: 700}}>
            <h1>Profile Page</h1>
            <p> Hello there, welcome</p>

            <button onClick={signOut}>Sign Out</button>
        </div>
      </>
    );
  }