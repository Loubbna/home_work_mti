class ProfileUpdateService:
    
    def update_member_profile(self, member, phone=None, membership_status=None, skills=None):

        if phone and not phone.isdigit():
            raise ValueError("Phone number must contain digits only.")
        
        if phone:
            member.phone = phone
        if membership_status:
            member.membership_status = membership_status
        if skills:
            member.skills = skills
        print(f"Profile updated for member: {member.last_name}")
