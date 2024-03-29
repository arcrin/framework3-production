from producer_consumer.result_processor import ResultProcessor
from producer_consumer.node_executor import NodeExecutor
from sample_profile.profile import SampleProfile
from node.base_node import BaseNode
from typing import List, Dict
import asyncio


class Application:
    def __init__(self):
        self._nodes: List[BaseNode] = []
        self._persist_nodes: Dict[str, BaseNode] = {}
        self._queue_for_execution: asyncio.Queue[BaseNode] = asyncio.Queue()
        self._queue_for_result_processing: asyncio.Queue[BaseNode] = asyncio.Queue()
        self._node_executor: NodeExecutor = NodeExecutor(
            self._queue_for_execution, self._queue_for_result_processing
        )
        self._result_processor: ResultProcessor = ResultProcessor(
            self._queue_for_result_processing
        )
        # self._dependency_checker: DependencyChecker = DependencyChecker(
        #     self._nodes, self._queue_for_execution
        # )

    async def add_node(self, node: BaseNode):
        self._nodes.append(node)
        node.set_on_ready_callback(self._node_ready)
        await node.notify_dependencies_resolved()

    async def _node_ready(self, node: BaseNode):
        await self._queue_for_execution.put(node)

    async def load_test_case(self):
        # LoadProfileNode should happen first, and it will return a the test jig class and profile class.
        # test jig class is used to initialize the hardware configuration of the test jig, profile class
        # is used to initialize the test cases. I need to create the dependencies among all of these tasks
        # and put them into a list.

        # I need to check if a node is ready to be put on the execution queue. I need to find a way to get around this.
        # load_test_case = LoadTCNode(self._nodes, SampleProfile)
        # await self._queue_for_execution.put(load_test_case)
        profile = SampleProfile()
        for tc_node in profile.test_case_list:
            await self.add_node(tc_node)

    @property
    def nodes(self) -> List[BaseNode]:
        return self._nodes

    async def start(self):
        await self.load_test_case()
        # self._dependency_checker.start_processing()
        # self._node_executor.start_processing()
        await asyncio.gather(
            # self._dependency_checker.start_processing(),
            self._node_executor.start_processing(),
            self._result_processor.start_processing(),
        )
