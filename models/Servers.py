from dataclasses import dataclass, field


@dataclass
class ServerData:
    common_name: str
    server_name: str
    _common_names: list[str] = field(init=False)
    _preferred_common_name: str = field(init=False)
    _server_name: str = field(init=False)

    def __post_init__(self):
        self._common_names = [self.common_name]

        # self.common_name =
        pass

    def __str__(self):
        return f"Server Common Name: {self._preferred_common_name}. Server Name: {self._server_name}"

    @property
    def common_name(self):
        return self._preferred_common_name

    @property
    def server_name(self):
        return self._server_name


    def add_comon_name(self, common_name):
        if common_name in self._common_names:
            raise ValueError(f"Common Name '{common_name}' already exists.")
        self._common_names.append(common_name)
        if self._preferred_common_name is None:
            self._preferred_common_name = common_name

    def select_preferred_common_name(self, common_name):
        if common_name in self._common_names:
            self._preferred_common_name = common_name
        else:
            raise ValueError(f"Common Name '{common_name}' not found in common names.")

    # @common_name.setter
    # def common_name(self, common_name):
    #     if len(common_name) > 100:
    #         raise ValueError("Common Name must be less than 100 characters.")
    #     self._common_name = common_name


if __name__ == "__main__":
    server_data = ServerData(common_name="Server1", server_name="SQLServer1")
    print(server_data.common_name)
    server_data.add_comon_name = "ServerABC"
    print(server_data.common_name)

    print(ServerData.server_name)
