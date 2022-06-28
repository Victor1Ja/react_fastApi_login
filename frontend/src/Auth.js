import { iseLocation, Navigate, useLocation } from "react-router-dom"

export const setToken = (token) => {
    localStorage.setItem("token", token);
}

export const getToken = () => {
    return localStorage.getItem("token");
}
// remove token from local storage
export const removeToken = () => {
    localStorage.removeItem("token");
}

export function RequireToken({children}){
    let auth = getToken();
    let location = useLocation();

    if(!auth){
        return <Navigate to='/' state={{form: location}} />;
    }
    return children;
}