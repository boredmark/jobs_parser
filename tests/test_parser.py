import sys
sys.path.append('/Users/valentyn/Documents/my_projects/jobs_parser')
import parser


def test_response_func():
	expect = 200
	p = parser.Parser('https://www.freelancer.com/jobs/')
	assert p.get_response().status_code == expect

def test_get_job_lins():
	expect = "<class 'list'>"
	p = parser.Parser('https://www.freelancer.com/jobs#')
	assert len(p.get_job_links()) > 0 
	assert str(type(p.get_job_links())) == expect

def test_get_all_info():
	p = parser.Parser('https://www.freelancer.com/jobs#')
	assert len(p.get_all_info()) > 0 
