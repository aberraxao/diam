import React, {useState} from "react";
import axios from 'axios';

axios.defaults.withCredentials = true
const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [msg, setMsg] = useState('');
    const [error, setError] = useState('');
    const handleLogin = async (e) => {
        e.preventDefault();
        try {
            const response = await axios.post(
                'http://localhost:8000/votacao/login/',
                {"username": username, "password": password},
            );
            if (response.status === 200) {
                localStorage.setItem('token', response.data.token);
                window.location.href = 'http://localhost:8000/votacao/index';
            } else {
                setError(response.data.error || response.data.error);
            }
        } catch (error) {
            console.error('Login falhou:', error);
            setError('Verifique as credenciais');
        }
    };

    return (
        <div className="container">
            <h1>Login</h1>
            <form onSubmit={handleLogin}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <br></br>
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <br></br>
                <p><small>
                    Não tem conta? <a href="http://localhost:8000/votacao/register">Registe aqui</a>
                </small></p>
                {error && <p>{error}</p>}
                {<p>{msg}</p>}
                <button type="submit">Login</button>
            </form>
        </div>
    );
};
export default Login;