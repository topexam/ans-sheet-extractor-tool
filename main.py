# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import logging
import math
from pathlib import Path
import time

import grpc
import main_pb2
import main_pb2_grpc
from src.entry import entry_point


class AnswerSheetExtractorServiceServicer(
    main_pb2_grpc.AnswerSheetExtractorServiceServicer
):
    """Provides methods that implement functionality of route guide server."""

    def extractAnswerSheet(self, request, context):
        entry_point(Path("inputs"))
        return main_pb2.ExtractAnswerSheetResponse(
            test_result_id="<empty>", images=[], user_answers=[]
        )


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    main_pb2_grpc.add_AnswerSheetExtractorServiceServicer_to_server(
        AnswerSheetExtractorServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
