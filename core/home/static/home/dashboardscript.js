const menuOpen = document.getElementById('menu-open');

// Function to fetch data and update the chart
function updateChart() {
    fetch('/api/data') // Replace with your API endpoint
        .then(response => response.json())
        .then(data => {
            // Update chart data and labels
            apiChart.data.labels.push(data.label); // Update with new label
            apiChart.data.datasets[0].data.push(data.value); // Update with new value
            apiChart.update();
        });
}

// Update the chart every 5 seconds
setInterval(updateChart, 5000);

 const menuClose = document.getElementById('menu-close');
 const sideBar = document.querySelector('.container .left-section');
 const sidebarItems = document.querySelectorAll('.container .left-section .sidebar .item');
 
 menuOpen.addEventListener('click', () => {
     sideBar.style.top = '0';
 });
 
 menuClose.addEventListener('click', () => {
     sideBar.style.top = '-60vh';
 });
 
 let activeItem = sidebarItems[0];
 
 sidebarItems.forEach(element => {
     element.addEventListener('click', () => {
         if (activeItem) {
             activeItem.removeAttribute('id');
         }
 
         element.setAttribute('id', 'active');
         activeItem = element;
 
     });
 });
