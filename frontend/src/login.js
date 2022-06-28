import { useNavigate } from "react-router-dom";
import {getToken} from "./Auth";
import { useState } from "react";
export default function Login(){
    const navigate = useNavigate();
    const [username,setUsername] = useState("");
    const [password,setPassword] = useState("");

    const login = () => {
        if( username == "" && password == ""){
            alert("Please enter username and password");
        }else{
            //api call to backend
            //if successfully logged in save the token in local storage

        }
    }
        return (
            <>
            <div style={{ minHeight: "800", marginTop: 30 }}>
                <h1>Login</h1>
                <div style={{ marginTop: 30 }}>
                    { getToken() ? (
                        <p>You are logged in :-)</p>                        
                    ) : (
                        <div>
                            <form>
                                <label style={{ marginRight: 10}}> Input Username</label> 
                                <input type="text" onChange={(e) => setUsername(e.target.value)} />

                                <label style={{ marginRight: 10}}> Input Password</label>
                                <input type="password" onChange={(e) => setPassword(e.target.value)} />

                                <button onClick={login}>Login</button>
                            </form>
                        </div>
                    )}
                </div>
            </div>
        </>
        );
}

    