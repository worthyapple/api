
    // Event Listener for Filters
    document.querySelectorAll('.filters input, .filters select').forEach(filter => {
        filter.addEventListener('change', function () {
            const dateFilter = document.getElementById('date-filter').value;
            const statusFilter = document.getElementById('status-filter').value;
            const methodFilter = document.getElementById('method-filter').value;

            // Logic to filter logs based on selected criteria
            filterLogs(dateFilter, statusFilter, methodFilter);
        });
    });

    function filterLogs(date, status, method) {
        const rows = document.querySelectorAll('.logs-table tbody tr');
        rows.forEach(row => {
            const logDate = row.cells[3].textContent; // Assuming timestamp is in the 4th column
            const logStatus = row.cells[2].textContent; // Assuming status code is in the 3rd column
            const logMethod = row.cells[1].textContent; // Assuming method is in the 2nd column

            const dateMatch = date ? logDate.includes(date) : true;
            const statusMatch = status !== 'all' ? logStatus === status : true;
            const methodMatch = method !== 'all' ? logMethod === method : true;

            if (dateMatch && statusMatch && methodMatch) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }

    document.querySelectorAll('.recent-ips .item').forEach(ipItem => {
        ipItem.addEventListener('click', function () {
            let selectedIP = this.getAttribute("data-ip");
            alert("Showing logs for IP: " + selectedIP);
            // Here, you can redirect to a detailed logs page or fetch logs dynamically
        });
    });
    // async function fetchLogs() {
    //     const response = await fetch('/api/logs/');
    //     const logs = await response.json();
    
    //     const logsTable = document.getElementById('logsTableBody');
    //     logsTable.innerHTML = '';
    
    //     logs.forEach(log => {
    //         const row = `
    //             <tr>
    //                 <td>${log.fields.user}</td>
    //                 <td>${log.fields.endpoint}</td>
    //                 <td>${log.fields.status_code}</td>
    //                 <td>${log.fields.timestamp}</td>
    //             </tr>
    //         `;
    //         logsTable.innerHTML += row;
    //     });
    // }
    
    // fetchLogs();