from descarteslabs.common.proto import job_pb2

from ..exceptions import JobComputeError
from ..job import Job


def test_init():
    message = job_pb2.Job(
        id="foo", error=job_pb2.JobError(code=job_pb2.ERROR_DEADLINE, message="bar")
    )

    job = Job(message)

    e = JobComputeError(job)
    assert e.code == job.error.code
    assert e.message == job.error.message
    assert e.id == job.id