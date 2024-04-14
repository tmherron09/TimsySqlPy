from dataclasses import dataclass, field


@dataclass
class ServerData:
    _common_name: str = field(init=False)
    _server_name: str = field(init=False)

    def __post_init__(self):

        # self.common_name =
        pass

    @property
    def common_name(self):
        return self._common_name

    @common_name.setter
    def common_name(self, common_name):
        if len(common_name) > 100:
            raise ValueError("Common Name must be less than 100 characters.")
        self._common_name = common_name


if __name__ == "__main__":
    server_data = ServerData(common_name="Server1")
    print(server_data.common_name)
    print(ServerData.server_name)