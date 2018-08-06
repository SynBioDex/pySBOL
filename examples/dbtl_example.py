"""This example script demonstrates pySBOL's API for workflow management by generating a hypothetical design-build-test-learn procedure."""
 
from sbol import *

doc=Document()
setHomespace('https://sys-bio.org')

doc = Document()

workflow_step_1 = Activity('build_1')
workflow_step_2 = Activity('build_2')
workflow_step_3 = Activity('build_3')
workflow_step_4 = Activity('build_4')
workflow_step_5 = Activity('build_5')
workflow_step_6 = Activity('test_1')
workflow_step_7 = Activity('analysis_1')

workflow_step_1.plan = Plan('PCR_protocol_part1')
workflow_step_2.plan = Plan('PCR_protocol_part2')
workflow_step_3.plan = Plan('PCR_protocol_part3')
workflow_step_4.plan = Plan('gibson_assembly')
workflow_step_5.plan = Plan('transformation')
workflow_step_6.plan = Plan('promoter_characterization')
workflow_step_7.plan = Plan('parameter_optimization')

setHomespace('')
Config.setOption('sbol_compliant_uris', False)  # Temporarily disable auto-construction of URIs

workflow_step_1.agent = Agent('mailto:jdoe@sbols.org')
workflow_step_2.agent = workflow_step_1.agent
workflow_step_3.agent = workflow_step_1.agent
workflow_step_4.agent = workflow_step_1.agent
workflow_step_5.agent = workflow_step_1.agent
workflow_step_6.agent = Agent('http://sys-bio.org/plate_reader_1')
workflow_step_7.agent = Agent('http://tellurium.analogmachine.org')

Config.setOption('sbol_compliant_uris', True)
setHomespace('https://sys-bio.org')

doc.addActivity([workflow_step_1, workflow_step_2, workflow_step_3, workflow_step_4, workflow_step_5, workflow_step_6, workflow_step_7])

target = Design('target')
part1 = workflow_step_1.generateBuild('part1', target)
part2 = workflow_step_2.generateBuild('part2', target)
part3 = workflow_step_3.generateBuild('part3', target)
gibson_mix = workflow_step_4.generateBuild('gibson_mix', target, [part1, part2, part3])
clones = workflow_step_5.generateBuild(['clone1', 'clone2', 'clone3'], target, gibson_mix)
experiment1 = workflow_step_6.generateTest('experiment1', clones)
analysis1 = workflow_step_7.generateAnalysis('analysis1', experiment1)

response = doc.write('dbtl.xml')
print(response)
