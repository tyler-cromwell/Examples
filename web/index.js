function box(name) {
    alert("Hello from "+ name); // Display alert box
    event.stopPropagation();    // Prevents onclick event from bubbling up to parents
}
