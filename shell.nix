with import <nixpkgs> {}; stdenv.mkDerivation {
  name = "env";
  buildInputs = [
    python35
    python35Packages.sympy
  ];
}
