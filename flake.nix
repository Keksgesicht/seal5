{
  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self, nixpkgs,
    flake-utils,
  }@inputs:

  flake-utils.lib.eachDefaultSystem
  (system:
    let
      pkgs = import inputs.nixpkgs {
        inherit system;
      };

      pyPkgs = pkgs.python311Packages;
      seal5PyPkgs = with pyPkgs; [
        dacite
        gitpython
        importlib-resources
        tqdm
        yamllint
      ];
    in
    {
      devShells.default = pkgs.mkShell {
        # virtualenv venv"
        # source venv/bin/activate
        # pip install -r requirements.txt
        # pip install -e .
        shellHook = ''
          source venv/bin/activate
        '';
        packages = seal5PyPkgs ++ [
          pyPkgs.virtualenv
          pkgs.cmake
          pkgs.gnumake
          pkgs.ninja
        ];
      };
    }
  );
}
