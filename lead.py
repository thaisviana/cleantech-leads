class Lead():
	def __init__(self, name=None, email=None, institution=None, description=None):
		self.name = name
		self.email = email
		self.institution = institution
		self.description = description

	def jsonify(obj):
		name = obj['name']
		email = obj['email']
		institution = obj['institution']
		description = obj['description']
		return {
                'name': name,
                'email': email,
                'institution': institution,
                'description': description
                }
