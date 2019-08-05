window.onload = function() {
    handler1 = function() {
        event.stopPropagation();    // Prevents onclick event from bubbling up to parents
        alert("Hello from Box 1");  // Display alert box
    }

    handler2 = function() {
        event.stopPropagation();    // Prevents onclick event from bubbling up to parents
        alert("Hello from Box 2");  // Display alert box
    }

    handler3 = function() {
        event.stopPropagation();    // Prevents onclick event from bubbling up to parents
        alert("Hello from Box 3");  // Display alert box
    }

    document.getElementById("Box 1").onclick = handler1;
    document.getElementById("Box 2").onclick = handler2;
    document.getElementById("Box 3").onclick = handler3;
}
