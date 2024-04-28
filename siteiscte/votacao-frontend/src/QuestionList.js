import React, {useState, useEffect} from 'react';
import axios from 'axios';

function QuestionList() {
    const [questoes, setQuestoes] = useState([]);
    useEffect(() => {
        axios.get("http://localhost:8000/votacao/api/questoes/")
            .then(res => {
                setQuestoes(res.data);
            });
    }, []);
    return (
        <>
            <h1>Lista de questões</h1>
            {questoes.map((q) => <p key={q.id}>{q.questao_texto}</p>)}
        </>
    )
}

export default QuestionList;