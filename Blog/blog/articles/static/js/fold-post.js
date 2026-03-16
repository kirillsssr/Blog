const foldBtns = document.getElementsByClassName("fold-button");

for (let i = 0; i < foldBtns.length; i++) {
    foldBtns[i].addEventListener("click", function (e) {
        const post = e.target.closest(".one-post");
        post.classList.toggle("folded");
        if (post.classList.contains("folded")) {
            e.target.innerHTML = "развернуть";
        } else {
            e.target.innerHTML = "свернуть";
        }
    });
}
