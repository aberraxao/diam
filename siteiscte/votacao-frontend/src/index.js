import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Login from "./Login";
import Contador from "./contador";
import MostraEEsconde from "./mostraeesconde";
import FormSimples from "./formsimples";

function App() {
    return (
        <div>
            <Login/>
            <Contador/>
            <MostraEEsconde/>
            <FormSimples/>
        </div>
    );
}

export default App;

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App/>);
