# This code is part of Qiskit.
#
# (C) Copyright IBM 2024.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.
"""Test qasmbench against abstract backend topologies"""

import pytest

from bqskit import compile
from bqskit.compiler import Compiler
from benchpress.utilities.io import qasm_circuit_loader
from benchpress.utilities.validation import circuit_validator
from benchpress.workouts.validation import benchpress_test_validation
from benchpress.config import Configuration
from benchpress.bqskit_gym.utils.bqskit_backend_utils import BqskitFlexibleBackend

from benchpress.workouts.abstract_transpile import (
    WorkoutAbstractQasmBenchSmall,
    WorkoutAbstractQasmBenchMedium,
    WorkoutAbstractQasmBenchLarge,
)
from benchpress.workouts.abstract_transpile.qasmbench import (
    SMALL_CIRC_TOPO,
    SMALL_NAMES,
    MEDIUM_CIRC_TOPO,
    MEDIUM_NAMES,
    LARGE_CIRC_TOPO,
    LARGE_NAMES,
)

OPTIMIZATION_LEVEL = Configuration.options["bqskit"]["optimization_level"]


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchSmall(WorkoutAbstractQasmBenchSmall):
    @pytest.mark.parametrize("circ_and_topo", SMALL_CIRC_TOPO, ids=SMALL_NAMES)
    def test_QASMBench_small(self, benchmark, circ_and_topo):
        circuit = qasm_circuit_loader(circ_and_topo[0], benchmark)
        BACKEND = BqskitFlexibleBackend(circuit.num_qudits, circ_and_topo[1])
        TWO_Q_GATE = BACKEND.two_q_gate_type
        compiler = Compiler()

        @benchmark
        def result():
            new_circ = compile(
                circuit,
                model=BACKEND,
                optimization_level=OPTIMIZATION_LEVEL,
                compiler=compiler,
            )
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.gate_counts[TWO_Q_GATE]
        benchmark.extra_info["depth_2q"] = result.multi_qudit_depth
        assert circuit_validator(result, BACKEND)


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchMedium(WorkoutAbstractQasmBenchMedium):
    @pytest.mark.parametrize("circ_and_topo", MEDIUM_CIRC_TOPO, ids=MEDIUM_NAMES)
    def test_QASMBench_medium(self, benchmark, circ_and_topo):
        circuit = qasm_circuit_loader(circ_and_topo[0], benchmark)
        BACKEND = BqskitFlexibleBackend(circuit.num_qudits, circ_and_topo[1])
        TWO_Q_GATE = BACKEND.two_q_gate_type
        compiler = Compiler()

        @benchmark
        def result():
            new_circ = compile(
                circuit,
                model=BACKEND,
                optimization_level=OPTIMIZATION_LEVEL,
                compiler=compiler,
            )
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.gate_counts[TWO_Q_GATE]
        benchmark.extra_info["depth_2q"] = result.multi_qudit_depth
        assert circuit_validator(result, BACKEND)


@benchpress_test_validation
class TestWorkoutAbstractQasmBenchLarge(WorkoutAbstractQasmBenchLarge):
    @pytest.mark.parametrize("circ_and_topo", LARGE_CIRC_TOPO, ids=LARGE_NAMES)
    def test_QASMBench_large(self, benchmark, circ_and_topo):
        circuit = qasm_circuit_loader(circ_and_topo[0], benchmark)
        BACKEND = BqskitFlexibleBackend(circuit.num_qudits, circ_and_topo[1])
        TWO_Q_GATE = BACKEND.two_q_gate_type
        compiler = Compiler()

        @benchmark
        def result():
            new_circ = compile(
                circuit,
                model=BACKEND,
                optimization_level=OPTIMIZATION_LEVEL,
                compiler=compiler,
            )
            return new_circ

        benchmark.extra_info["gate_count_2q"] = result.gate_counts[TWO_Q_GATE]
        benchmark.extra_info["depth_2q"] = result.multi_qudit_depth
        assert circuit_validator(result, BACKEND)
