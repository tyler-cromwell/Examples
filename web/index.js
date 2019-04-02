window.onload = function() {
    handler1 = function box(e) {
        event.stopPropagation();    // Prevents onclick event from bubbling up to parents
        alert("Hello from Box 1");  // Display alert box
    }

    handler2 = function box(e) {
        event.stopPropagation();    // Prevents onclick event from bubbling up to parents
        alert("Hello from Box 2");  // Display alert box
    }

    handler3 = function box(e) {
        event.stopPropagation();    // Prevents onclick event from bubbling up to parents
        alert("Hello from Box 3");  // Display alert box
    }

    document.getElementById("Box 1").addEventListener("click", handler1);
    document.getElementById("Box 2").addEventListener("click", handler2);
    document.getElementById("Box 3").addEventListener("click", handler3);
}
