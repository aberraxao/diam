function Header() {
    // Estilos CSS
    const separador = {
        color: "white", backgroundColor: "DodgerBlue",
        margin: "0", height: "5vh",
    };
    const contentor = {
        color: "DodgerBlue", backgroundColor: "LightBlue",
        margin: "0", height: "20vh",
        display: "flex", justifyContent: "center", alignItems: "center",
    };
    return (
        <>
            <div style={separador}/>
            <div style={contentor}>
                <h1>Isto seria o header</h1>
            </div>
            <div style={separador}/>
        </>
    )
}

export default Header
