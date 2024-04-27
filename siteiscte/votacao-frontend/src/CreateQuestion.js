import React, {useState} from 'react';
import axios from 'axios';
import moment from 'moment';

function CreateQuestion() {
    const [questaoTexto, setQuestaoTexto] = useState("");
    const changeHandler = (e) => {
        setQuestaoTexto(e.target.value);
    }
    const submitHandler = (e) => {
        e.preventDefault();
        const pubData = moment(Date.now()).format('YYYY-MM-DD HH:mm');
        axios.post("http://localhost:8000/votacao/api/questoes/", {
            "questao_texto": questaoTexto,
            "pub_data": pubData
        }).then();
    }
    return (
        <> <h1>Inserir uma nova questão</h1>
            <form onSubmit={submitHandler}>
                <label>Texto da questão:</label>
                <input type="text" value={questaoTexto} onChange={changeHandler}/>
                <br/><br/>
                <input type="submit" value="Submeter"/>
            </form>
        </>
    );
}

export default CreateQuestion;