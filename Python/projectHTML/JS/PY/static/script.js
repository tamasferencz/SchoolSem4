function startGame() {
    const customWord = document.getElementById("customWord").value;
    if (!customWord) {
        alert("Please enter a word!");
        return;
    }

    fetch('/start_game', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ word: customWord })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("setup").style.display = "none";
                document.getElementById("game").style.display = "block";
                document.getElementById("hangmanCanvas").style.display = "block";
                document.getElementById("word").innerText = data.display_word;
                document.getElementById("wrong").innerText = "Wrong guesses: ";
                document.getElementById("message").innerText = "";
            }
        });
}

function drawBaseStructure() {
    const canvas = document.getElementById("hangmanCanvas");
    const ctx = canvas.getContext("2d");

    ctx.clearRect(0, 0, canvas.width, canvas.height);

    // Base
    ctx.beginPath();
    ctx.moveTo(20, 230);
    ctx.lineTo(180, 230);
    ctx.stroke();

    // Pole
    ctx.beginPath();
    ctx.moveTo(50, 230);
    ctx.lineTo(50, 20);
    ctx.stroke();

    // Top bar
    ctx.beginPath();
    ctx.moveTo(50, 20);
    ctx.lineTo(130, 20);
    ctx.stroke();

    // Rope
    ctx.beginPath();
    ctx.moveTo(130, 20);
    ctx.lineTo(130, 50);
    ctx.stroke();
}

function drawHangman(wrongCount) {
    const canvas = document.getElementById("hangmanCanvas");
    const ctx = canvas.getContext("2d");

    if (wrongCount > 0) {
        ctx.beginPath();  // Head
        ctx.arc(130, 70, 20, 0, Math.PI * 2);
        ctx.stroke();
    }
    if (wrongCount > 1) {
        ctx.beginPath();  // Body
        ctx.moveTo(130, 90);
        ctx.lineTo(130, 150);
        ctx.stroke();
    }
    if (wrongCount > 2) {
        ctx.beginPath();  // Left Arm
        ctx.moveTo(130, 110);
        ctx.lineTo(100, 130);
        ctx.stroke();
    }
    if (wrongCount > 3) {
        ctx.beginPath();  // Right Arm
        ctx.moveTo(130, 110);
        ctx.lineTo(160, 130);
        ctx.stroke();
    }
    if (wrongCount > 4) {
        ctx.beginPath();  // Left Leg
        ctx.moveTo(130, 150);
        ctx.lineTo(100, 190);
        ctx.stroke();
    }
    if (wrongCount > 5) {
        ctx.beginPath();  // Right Leg
        ctx.moveTo(130, 150);
        ctx.lineTo(160, 190);
        ctx.stroke();
    }
}

function makeGuess() {
    const letter = document.getElementById("letter").value;
    fetch('/guess', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ letter: letter })
    })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById("word").innerText = data.display_word;
                document.getElementById("wrong").innerText = "Wrong guesses: " + data.wrong_guesses.join(", ");
                document.getElementById("message").innerText = data.won ? "You win!" : (data.lost ? "You lose!" : "");
                drawHangman(data.wrong_guesses.length);
            } else {
                alert(data.message);
            }
        });
}


function newGame() {
    document.getElementById("setup").style.display = "block";
    document.getElementById("game").style.display = "none";
    document.getElementById("customWord").value = "";
    drawBaseStructure();
}

window.onload = function () {
    drawBaseStructure();
}