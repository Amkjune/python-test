import xml.etree.ElementTree as ET

xml_content = '''
<root xmlns:jcr="http://www.jcp.org/jcr/1.0"
      xmlns:cq="http://www.day.com/jcr/cq/1.0"
      xmlns:dam="http://www.day.com/jcr/dam/1.0"
      xmlns:icr="http://www.example.com/icr"
      xmlns:jer="http://www.example.com/jer"
      >

    <jcr:content
        cq:lastReplicated="(Date)2019-02-09T07:30:34.92ez"
        cq:lastReplicatedBy="sumit.dhage@net-effect.com"
        cq:lastReplicationAction="Activate"
        dam:assetstate="processing"
        dam:relativePath="pwc/rm/en/assets/eiffel-tower-jpg"
        icr:lastModified="(Date)2019-02-09T05:28:47.2882"
        jcr:lastModifiedBy="debayan.dasgupta@in.pwc.com"
        jcr:mixinTypes="[cq:Replicationstatus]"
        jcr:primaryType="dam:Assetcontent">
        <metadata 
            dam:Bitsperpixel="{Long}24" 
            dam:extracted="{Date}2019-02-09T05:28:46.302Z"
            dam:Fileformat="JPEG"
            dam:MIMEtype="image/jpeg"
            dam:Numberofimages="{Long}1"
            dam:Physicalwidthininches="{Decimal}-1.0"
            dam:Progressive="yes"
            dam:sha1="df33b8c6d43969d90d632d164d6b48cfaf421dda"
            dam:size="{Long}117084"
            
            />
        
    </jcr:content>
    <mytag>
    </mytag>
</root>
'''

# Parse the XML content
root = ET.fromstring(xml_content)


properties = {}
for elem in root.iter('{http://www.jcp.org/jcr/1.0}content'):
    # Extract only the local name (without namespace prefix) and print each property in a separate row
    for key, value in elem.attrib.items():
        local_name = key.split('}')[-1]
        print(f"{local_name}: {value}")

metadata_properties = {}
for elem in root.findall('.//jcr:content/metadata', namespaces={'jcr': 'http://www.jcp.org/jcr/1.0'}):
   
    for key, value in elem.attrib.items():
        metadata_properties[key] = value

# Print properties line by line
for key, value in metadata_properties.items():
    local_name = key.split('}')[-1]
    print(f"{local_name}: {value}")
    

    

