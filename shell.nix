with import <nixpkgs> {};
let
  pyeclib = callPackage ../pyeclib {};
in stdenv.mkDerivation {
  name = "env";
  buildInputs = with python3Packages; [
    sympy
    pyeclib
    python3
    notebook
    jupyter_console
    nbconvert
    ipykernel
    ipywidgets
  ];
}
