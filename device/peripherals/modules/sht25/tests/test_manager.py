# Import standard python libraries
import os, sys, json

# Set system path and directory
root_dir = os.environ["OPENAG_BRAIN_ROOT"]
sys.path.append(root_dir)
os.chdir(root_dir)

# Import device utilities
from device.utilities.accessors import get_peripheral_config
from device.utilities.modes import Modes

# Import device state
from device.state import State

# Import simulators
from device.comms.i2c2.mux_simulator import MuxSimulator

# Import peripheral manager
from device.peripherals.modules.sht25.manager import SHT25Manager

# Load test config
path = root_dir + "/device/peripherals/modules/sht25/tests/config.json"
device_config = json.load(open(path))
peripheral_config = get_peripheral_config(device_config["peripherals"], "SHT25-Top")


def test_init() -> None:
    manager = SHT25Manager(
        name="Test",
        state=State(),
        config=peripheral_config,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )


def test_initialize() -> None:
    manager = SHT25Manager(
        name="Test",
        state=State(),
        config=peripheral_config,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    manager.initialize()


def test_setup() -> None:
    manager = SHT25Manager(
        name="Test",
        state=State(),
        config=peripheral_config,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    manager.initialize()
    manager.setup()


def test_update() -> None:
    manager = SHT25Manager(
        name="Test",
        state=State(),
        config=peripheral_config,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    manager.initialize()
    manager.update()


def test_reset() -> None:
    manager = SHT25Manager(
        name="Test",
        state=State(),
        config=peripheral_config,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    manager.initialize()
    manager.reset()


def test_shutdown() -> None:
    manager = SHT25Manager(
        name="Test",
        state=State(),
        config=peripheral_config,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    manager.initialize()
    manager.shutdown()


def test_turn_on() -> None:
    manager = SHT25Manager(
        name="Test",
        state=State(),
        config=peripheral_config,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    manager.initialize()

    # Try to turn on outside manual mode
    manager.mode = Modes.NORMAL
    manager.process_event(request={"type": "Turn On"})
    assert manager.response["status"] == 400

    # Turn on from manual mode
    manager.mode = Modes.MANUAL
    manager.process_event(request={"type": "Turn On"})
    assert manager.response["status"] == 200


def test_turn_off() -> None:
    manager = SHT25Manager(
        name="Test",
        state=State(),
        config=peripheral_config,
        simulate=True,
        mux_simulator=MuxSimulator(),
    )
    manager.initialize()

    # Try to turn off outside manual mode
    manager.mode = Modes.NORMAL
    manager.process_event(request={"type": "Turn Off"})
    assert manager.response["status"] == 400

    # Turn off from manual mode
    manager.mode = Modes.MANUAL
    manager.process_event(request={"type": "Turn Off"})
    assert manager.response["status"] == 200
