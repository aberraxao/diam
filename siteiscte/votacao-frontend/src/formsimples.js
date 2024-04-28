import React, {useState} from "react";

function FormSimples() {
    const [nome, setNome] = useState("");
    const changeHandler = (evento) => {
        setNome(evento.target.value);
    }
    const submitHandler = () => {
        alert("Sim, tu és " + nome);
    }
    return (
        <div className="container">
            <form onSubmit={submitHandler}>
                <h1><label>Quem és tu?</label></h1>
                <input type="text" name="nome" value={nome} onChange={changeHandler}/>
                <input type="submit" value="Sou mesmo?"/>
            </form>
        </div>
    );
}

export default FormSimples;