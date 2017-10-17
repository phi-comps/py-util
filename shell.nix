with import <nixpkgs> {}; stdenv.mkDerivation {
  name = "env";
  buildInputs = [
    eclib
    python35
    python35Packages.sympy
    python35Packages.ipython
    python35Packages.jupyter
  ];
}
