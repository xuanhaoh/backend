from server.app.vfg.parser.Plan_generator import get_plan
from server.app.vfg.parser.Domain_parser import get_domain_json
from server.app.vfg.parser.Problem_parser import *
from server.app.vfg.parser.Animation_parser import get_animation_profile
from server.app.vfg.parser.Predicates_generator import *
from server.app.vfg.solver.Solver import get_visualisation_dic
from server.app.vfg.solver.Initialise import initialise_objects
from server.app.vfg.adapter.visualiser_adapter.Transfer import generate_visualisation_file
import json

url_link = ''
animation_content = open('domain_ap.pddl', 'r', encoding='utf-8-sig').read()
domain_content = open('domain.pddl', 'r', encoding='utf-8-sig').read().lower()
problem_content = open('problem12.pddl', 'r', encoding='utf-8-sig').read().lower()
plan = get_plan(domain_content, problem_content, url_link)
predicates_list = get_domain_json(domain_content)
problem_dic = get_problem_dic(problem_content, predicates_list)
object_list = get_object_list(problem_content)
animation_profile = json.loads(get_animation_profile(animation_content, object_list))
stages = new_get_stages(plan, problem_dic, problem_content, predicates_list)
result = get_visualisation_dic(stages, animation_profile, plan['result']['plan'], problem_dic)
objects_dic = initialise_objects(stages["objects"], animation_profile)
final = generate_visualisation_file(result, list(objects_dic.keys()), animation_profile, plan['result']['plan'])
with open("test.vfg", "w") as f:
    json.dump(final, f)

# actionlist = plan['result']['plan']
# print(actionlist)
# action_effect_list = get_action_effect_list(actionlist)
# print(predicates_list)
# for counter in range(len(actionlist)):
#     add_result, remove_result = new_get_state_list(predicates_list, action_effect_list[counter])
#     print(add_result)
#     print(remove_result)