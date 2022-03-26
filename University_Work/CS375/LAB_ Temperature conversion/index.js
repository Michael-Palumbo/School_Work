function ConvertCtoF(degreesCelsius) {
    return degreesCelsius * 9.0 / 5.0 + 32
}

function ConvertFtoC(degreesFahrenheit) {
    return (degreesFahrenheit - 32) * 5.0 / 9.0
}

function bodyLoaded() {
    var button = document.getElementById("ConvertButton");
    button.addEventListener( "click", convertJawn);
    document.getElementById("CInput").addEventListener( "input", () => document.getElementById("FInput").value = "");
    document.getElementById("FInput").addEventListener( "input", () => document.getElementById("CInput").value = "");
    //console.log("Reached bodyLoaded");
}

function convertJawn(Event){
	console.log("Clicked")
	CInp = document.getElementById("CInput")
	FInp = document.getElementById("FInput")

	if ( CInp.value != "" && FInp.value == "" && checkInp(CInp.value)){
		FInp.value = ConvertCtoF(parseFloat(CInp.value))
		updateImage(FInp.value)
	}else if( FInp.value != "" && CInp.value == "" && checkInp(FInp.value)){
		CInp.value = ConvertFtoC(parseFloat(FInp.value))
		updateImage(FInp.value)
	}
}

function checkInp(theValue){
	if (Number.isNaN(parseFloat(theValue))){
		//console.log("Reached")
		document.getElementById("ErrDiv").innerText = `${theValue} is not a number`
		return false
	}
	document.getElementById("ErrDiv").innerText = ""
	return true
}

function updateImage(F){
	var image = document.getElementById("WeatherImage")
	if (F > 50)
		image.src = "warm.gif"
	else if (F < 32)
		image.src = "cold.gif"
	else
		image.src = "cool.gif"
}