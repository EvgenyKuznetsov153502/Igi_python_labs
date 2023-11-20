    function generateTable() {
        const size = document.getElementById("sizeInput").value;
        const table = document.getElementById("myTable");
        table.innerHTML = "";

        for (let i = 0; i < size; i++) {
            const row = table.insertRow();
            for (let j = 0; j < size; j++) {
                const cell = row.insertCell();
                cell.textContent = Math.floor(Math.random() * 10) + 1;
                cell.addEventListener("click", function () {
                    toggleCellColor(cell);
                });
            }
        }
    }

    function transposeTable() {
        const table = document.getElementById("myTable");
        const rows = table.rows;
        const cols = rows[0].cells.length;

        const newTable = document.createElement("table");

        for (let i = 0; i < cols; i++) {
            const newRow = newTable.insertRow();
            for (let j = 0; j < rows.length; j++) {
                const newCell = newRow.insertCell();
                newCell.textContent = rows[j].cells[i].textContent;
            }
        }

        table.innerHTML = newTable.innerHTML;
        updateEventListeners();
    }

    function updateEventListeners() {
        const cells = document.querySelectorAll("#myTable td");
        cells.forEach(cell => {
            cell.addEventListener("click", function () {
                toggleCellColor(cell);
            });
        });
    }

    function toggleCellColor(cell) {
        const n = document.getElementById("nInput").value;
        const row = cell.parentNode;
        const colIndex = cell.cellIndex;

        const selectedInRow = Array.from(row.cells).filter(c => c.classList.contains("selected")).length;
        const selectedInCol = Array.from(cell.parentNode.parentNode.rows).filter(r => r.cells[colIndex].classList.contains("selected")).length;

        if (!cell.classList.contains("selected") && selectedInRow < n && selectedInCol < n) {
            const number = parseInt(cell.textContent, 10);

            if (number % 2 === 0) {
                cell.classList.add("selected", "even");
            } else {
                cell.classList.add("selected", "odd");
            }
        } else if (cell.classList.contains("selected")) {
            cell.classList.remove("selected", "even", "odd");
        } else {
            alert(`Максимальное количество выделенных ячеек в ряду/столбце: ${n}`);
        }
    }

    function addRow() {
        const table = document.getElementById("myTable");
        const newRow = table.insertRow();
        const cols = table.rows[0].cells.length;

        for (let i = 0; i < cols; i++) {
            const newCell = newRow.insertCell();
            newCell.textContent = Math.floor(Math.random() * 10) + 1;
            newCell.addEventListener("click", function () {
                toggleCellColor(newCell);
            });
        }
    }

    function addColumn() {
        const table = document.getElementById("myTable");
        const rows = table.rows;

        for (let i = 0; i < rows.length; i++) {
            const newCell = rows[i].insertCell();
            newCell.textContent = Math.floor(Math.random() * 10) + 1;
            newCell.addEventListener("click", function () {
                toggleCellColor(newCell);
            });
        }
    }