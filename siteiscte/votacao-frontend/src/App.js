import './App.css';
import Login from "./Login";
import Contador from "./contador";
import MostraEEsconde from "./mostraeesconde";
import FormSimples from "./formsimples";

function App() {
    return (
        <div className="App">
            <Login/>
            <Contador/>
            <MostraEEsconde/>
            <FormSimples/>
        </div>
    );
}

export default App;
