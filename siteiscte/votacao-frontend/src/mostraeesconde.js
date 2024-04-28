import React, {useState} from 'react';
import leaoSrc from './leao.jpg';

function MostraEEsconde() {
    const [texto, setTexto] = useState(true);

    const alternarVisibilidade = () => {
        setTexto(!texto);
    };

    return (
        <div className="container">
            <h1>
                <button onClick={alternarVisibilidade}>Mostrar / Esconder</button>
            </h1>
            {texto && <p>Eu sou o texto e estou à mostra!</p>}
            {!texto && <img src={leaoSrc} alt="Leao" style={{width: '300px', height: 'auto'}}/>}
        </div>
    );
}

export default MostraEEsconde;
