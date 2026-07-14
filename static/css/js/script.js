alert("Il file funziona!");
let step = 0;

const steps = [
    {
        title: "5 cose che riesci a vedere",
        text: "Guarda lentamente intorno a te. Trova 5 cose che riesci a vedere."
    },
    {
        title: "4 cose che puoi toccare",
        text: "Concentrati su 4 cose che puoi sentire con il tatto."
    },
    {
        title: "3 cose che puoi sentire",
        text: "Ascolta attentamente e trova 3 suoni intorno a te."
    },
    {
        title: "2 cose che puoi annusare",
        text: "Trova 2 profumi o odori vicino a te."
    },
    {
        title: "1 cosa che puoi assaporare",
        text: "Concentrati su un sapore o su una sensazione piacevole."
    },
    {
        title: "Bravissima ❤️",
        text: "Hai fatto un passo importante. Respira, questo momento passerà."
    }
];


function nextStep() {

    step++;

    document.getElementById("step-title").innerText = steps[step].title;

    document.getElementById("step-text").innerText = steps[step].text;


    if (step === steps.length - 1) {
        document.getElementById("continue-btn").style.display = "none";
    }
 }
