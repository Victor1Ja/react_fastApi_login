import { useNavigate } from "react-router-dom";
import {getToken, setToken} from "./Auth";
import { useState } from "react";
import axios from "axios";


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
            axios.post("http://localhost:8001/login",{
                username: username,
                email: username,
                password: password,
            }).then(function (response) {
            console.log(response.data.token, "response.data.token");
            
            if( response.data.token){
                setToken(response.data.token);
                navigate("/profile");
            }else{
                alert("Invalid username or password");
            }

            })
            .catch(function (error) {
                console.log(error);
            });


        }
    }
        return (
            <>
            <div style={{ minHeight: "800", marginTop: 30 }}>
                <h1>Login</h1>
                <div style={{ marginTop: 30 }}>
                    { getToken() ? (
                        <div>
                            <p>You are logged in :-)</p>
                            <button> <a href="/profile"> Profile</a></button>
                        </div>
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

    