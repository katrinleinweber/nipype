# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..utils import PowerSpectrum


def test_PowerSpectrum_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=0,
        ),
        out_file=dict(
            argstr='%s',
            genfile=True,
            hash_files=False,
            position=1,
        ),
        output_type=dict(),
    )
    inputs = PowerSpectrum.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_PowerSpectrum_outputs():
    output_map = dict(out_file=dict(), )
    outputs = PowerSpectrum.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
