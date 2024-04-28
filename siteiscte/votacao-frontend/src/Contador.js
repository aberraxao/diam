import React, { useState } from 'react';

function Contador() {
  const [contador, setContador] = useState(0);

  const incrementarContador = () => {
    setContador(contador + 1);
  };

  return (
      <div className="container">
          <h1><strong>Contador:</strong> {contador}</h1>
          <button onClick={incrementarContador}>Incrementar</button>
      </div>
  );
}

export default Contador;