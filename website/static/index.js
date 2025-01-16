function deleteNote(noteId) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}

function updateNote(noteId,rating) {
    fetch("/update-note", {
        method: "POST",
        body: JSON.stringify({ noteId: noteId, rating: rating }),
    }).then((_res) => {
        window.location.href = "/";
    });
}