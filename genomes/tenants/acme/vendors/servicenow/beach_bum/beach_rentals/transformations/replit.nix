{ pkgs }: {
  deps = [
    pkgs.python311Full
    pkgs.python311Packages.fastapi
    pkgs.python311Packages.uvicorn
    pkgs.python311Packages.pydantic
    pkgs.python311Packages.aiofiles
    pkgs.python311Packages.jinja2
    pkgs.python311Packages.httpx
    pkgs.python311Packages.sqlalchemy
  ];
}