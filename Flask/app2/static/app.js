function deletePerson(pid) {
    console.log("deletePerson called with ID:", pid); // Debugging

    // Construct the URL for the DELETE request
    const url = `/delete/${pid}`;
    console.log('Request URL:', url); // Debugging

    // Perform the DELETE request
    fetch(url, {
        method: 'DELETE'
    })
    .then(response => {
        if (response.ok) {
            console.log(`Person with ID ${pid} deleted successfully!`);
            window.location.reload(); // Reload the page to update the list
        } else {
            console.error(`Failed to delete person with ID: ${pid}. Status: ${response.status}`);
            alert('Failed to delete the person. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error during fetch:', error);
        alert('An error occurred. Please try again.');
    });
}

