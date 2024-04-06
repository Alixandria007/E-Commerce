function irParaLink() {
    var select = document.getElementById("conta");
    var selectedOption = select.options[select.selectedIndex];
    var url = selectedOption.value;
      window.location.href = url;
  }
