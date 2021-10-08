import pytest

from tribler_core.components.base import Session
from tribler_core.components.ipv8.ipv8_component import Ipv8Component
from tribler_core.components.libtorrent.libtorrent_component import LibtorrentComponent
from tribler_core.components.masterkey.masterkey_component import MasterKeyComponent
from tribler_core.components.metadata_store.metadata_store_component import MetadataStoreComponent
from tribler_core.components.popularity.popularity_component import PopularityComponent
from tribler_core.components.restapi import RESTComponent
from tribler_core.components.socks_configurator import SocksServersComponent
from tribler_core.components.torrent_checker import TorrentCheckerComponent


# pylint: disable=protected-access


@pytest.mark.asyncio
async def test_popularity_component(tribler_config):
    components = [SocksServersComponent(), LibtorrentComponent(), TorrentCheckerComponent(), MetadataStoreComponent(),
                  MasterKeyComponent(), RESTComponent(), Ipv8Component(), PopularityComponent()]
    session = Session(tribler_config, components)
    with session:
        await session.start()

        comp = PopularityComponent.instance()
        assert comp.community
        assert comp._ipv8_component

        await session.shutdown()
