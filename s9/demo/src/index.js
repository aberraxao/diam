import React from 'react';
import ReactDOM from 'react-dom/client';
import Header from './Header.js'

function IndexPage() {
    return (
        <>
            <Header/>
            <h1>E agora vem aqui mais qq coisa!</h1>
        </>
    )
}

ReactDOM.createRoot(document.getElementById('root')).render(<IndexPage/>);
