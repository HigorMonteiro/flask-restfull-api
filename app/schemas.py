from flask_restful import fields

user_fields = {
    "email": fields.String,
}

letter_fields = {
    "email": fields.String,
    "name": fields.String,
    "message": fields.String,
    "send_email": fields.Nested(user_fields),
    "reference_id": fields.String,
}
