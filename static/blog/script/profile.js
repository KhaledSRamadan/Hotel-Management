function toggleVisa() {
  let div = document.getElementById("toggle-tab");
  if (
    div.style.maxHeight === "0px" ||
    div.style.maxHeight === "" ||
    div.style.maxHeight === "0"
  ) {
    div.style.maxHeight = "500px";
  } else {
    div.style.maxHeight = "0px";
  }
}
