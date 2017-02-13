""" system field definitions (cannot be dynamically pulled but are available) """

CONTACT_SYSTEM_FIELDS = [
    {"name": "contactID", "statement": "{{Contact.Id}}"},
    {"name": "createdAt", "statement": "{{Contact.CreatedAt}}"},
    {"name": "updatedAt", "statement": "{{Contact.UpdatedAt}}"},
    {"name": "isSubscribed", "statement": "{{Contact.Email.IsSubscribed}}"},
    {"name": "isBounced", "statement": "{{Contact.Email.IsBounced}}"}
]

ACCOUNT_SYSTEM_FIELDS = [
    {"name": "accountID", "statement": "{{Account.Id}}"},
    {"name": "createdAt", "statement": "{{Account.CreatedAt}}"},
    {"name": "updatedAt", "statement": "{{Account.UpdatedAt}}"}
]

ACTIVITY_FIELDS = {
    "EmailOpen": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "EmailAddress",
         "statement": "{{Activity.Field(EmailAddress)}}"},
        {"name": "ContactId", "statement": "{{Activity.Contact.Id}}"},
        {"name": "IpAddress", "statement": "{{Activity.Field(IpAddress)}}"},
        {"name": "VisitorId", "statement": "{{Activity.Visitor.Id}}"},
        {"name": "EmailRecipientId",
         "statement": "{{Activity.Field(EmailRecipientId)}}"},
        {"name": "AssetType", "statement": "{{Activity.Asset.Type}}"},
        {"name": "AssetName", "statement": "{{Activity.Asset.Name}}"},
        {"name": "AssetId", "statement": "{{Activity.Asset.Id}}"},
        {"name": "SubjectLine",
         "statement": "{{Activity.Field(SubjectLine)}}"},
        {"name": "EmailWebLink",
         "statement": "{{Activity.Field(EmailWebLink)}}"},
        {"name": "VisitorExternalId", "statement": "{{Activity.Visitor.ExternalId}}"},
        {"name": "CampaignId", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"},
        {"name": "DeploymentId",
         "statement": "{{Activity.Field(EmailDeploymentId)}}"},
        {"name": "EmailSendType",
         "statement": "{{Activity.Field(EmailSendType)}}"}
    ],
    "EmailClickthrough": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "EmailAddress",
         "statement": "{{Activity.Field(EmailAddress)}}"},
        {"name": "ContactId", "statement": "{{Activity.Contact.Id}}"},
        {"name": "IpAddress", "statement": "{{Activity.Field(IpAddress)}}"},
        {"name": "VisitorId", "statement": "{{Activity.Visitor.Id}}"},
        {"name": "EmailRecipientId",
         "statement": "{{Activity.Field(EmailRecipientId)}}"},
        {"name": "AssetType", "statement": "{{Activity.Asset.Type}}"},
        {"name": "AssetName", "statement": "{{Activity.Asset.Name}}"},
        {"name": "AssetId", "statement": "{{Activity.Asset.Id}}"},
        {"name": "SubjectLine",
         "statement": "{{Activity.Field(SubjectLine)}}"},
        {"name": "EmailWebLink",
         "statement": "{{Activity.Field(EmailWebLink)}}"},
        {"name": "EmailClickedThruLink",
         "statement": "{{Activity.Field(EmailClickedThruLink)}}"},
        {"name": "VisitorExternalId", "statement": "{{Activity.Visitor.ExternalId}}"},
        {"name": "CampaignId", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"},
        {"name": "DeploymentId",
         "statement": "{{Activity.Field(EmailDeploymentId)}}"},
        {"name": "EmailSendType",
         "statement": "{{Activity.Field(EmailSendType)}}"}
    ],
    "EmailSend": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "EmailAddress",
         "statement": "{{Activity.Field(EmailAddress)}}"},
        {"name": "ContactId", "statement": "{{Activity.Contact.Id}}"},
        {"name": "EmailRecipientId",
         "statement": "{{Activity.Field(EmailRecipientId)}}"},
        {"name": "AssetType", "statement": "{{Activity.Asset.Type}}"},
        {"name": "AssetId", "statement": "{{Activity.Asset.Id}}"},
        {"name": "AssetName", "statement": "{{Activity.Asset.Name}}"},
        {"name": "SubjectLine",
         "statement": "{{Activity.Field(SubjectLine)}}"},
        {"name": "EmailWebLink",
         "statement": "{{Activity.Field(EmailWebLink)}}"},
        {"name": "CampaignId", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"},
        {"name": "DeploymentId",
         "statement": "{{Activity.Field(EmailDeploymentId)}}"},
        {"name": "EmailSendType",
         "statement": "{{Activity.Field(EmailSendType)}}"}
    ],
    "Subscribe": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "AssetId", "statement": "{{Activity.Asset.Id}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "EmailAddress",
         "statement": "{{Activity.Field(EmailAddress)}}"},
        {"name": "EmailRecipientId",
         "statement": "{{Activity.Field(EmailRecipientId)}}"},
        {"name": "AssetType", "statement": "{{Activity.Asset.Type}}"},
        {"name": "AssetName", "statement": "{{Activity.Asset.Name}}"},
        {"name": "CampaignId", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"}
    ],
    "Unsubscribe": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "AssetId", "statement": "{{Activity.Asset.Id}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "EmailAddress",
         "statement": "{{Activity.Field(EmailAddress)}}"},
        {"name": "EmailRecipientId",
         "statement": "{{Activity.Field(EmailRecipientId)}}"},
        {"name": "AssetType", "statement": "{{Activity.Asset.Type}}"},
        {"name": "AssetName", "statement": "{{Activity.Asset.Name}}"},
        {"name": "CampaignId", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"}
    ],
    "Bounceback": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "EmailAddress",
         "statement": "{{Activity.Field(EmailAddress)}}"},
        {"name": "AssetId", "statement": "{{Activity.Asset.Id}}"},
        {"name": "AssetType", "statement": "{{Activity.Asset.Type}}"},
        {"name": "AssetName", "statement": "{{Activity.Asset.Name}}"},
        {"name": "CampaignId", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"}
    ],
    "WebVisit": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "ContactId", "statement": "{{Activity.Contact.Id}}"},
        {"name": "VisitorId", "statement": "{{Activity.Visitor.Id}}"},
        {"name": "VisitorExternalId", "statement": "{{Activity.Visitor.ExternalId}}"},
        {"name": "ReferrerUrl",
         "statement": "{{Activity.Field(ReferrerUrl)}}"},
        {"name": "IpAddress", "statement": "{{Activity.Field(IpAddress)}}"},
        {"name": "NumberOfPages",
         "statement": "{{Activity.Field(NumberOfPages)}}"},
        {"name": "FirstPageViewUrl",
         "statement": "{{Activity.Field(FirstPageViewUrl)}}"},
        {"name": "Duration", "statement": "{{Activity.Field(Duration)}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"}
    ],
    "PageView": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "ContactId", "statement": "{{Activity.Contact.Id}}"},
        {"name": "CampaignId", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "VisitorId", "statement": "{{Activity.Visitor.Id}}"},
        {"name": "VisitorExternalId", "statement": "{{Activity.Visitor.ExternalId}}"},
        {"name": "WebVisitId", "statement": "{{Activity.Field(WebVisitId)}}"},
        {"name": "Url", "statement": "{{Activity.Field(Url)}}"},
        {"name": "ReferrerUrl",
         "statement": "{{Activity.Field(ReferrerUrl)}}"},
        {"name": "IpAddress", "statement": "{{Activity.Field(IpAddress)}}"},
        {"name": "IsWebTrackingOptedIn",
         "statement": "{{Activity.Field(IsWebTrackingOptedIn)}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"}
    ],
    "FormSubmit": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "ContactId", "statement": "{{Activity.Contact.Id}}"},
        {"name": "VisitorId", "statement": "{{Activity.Visitor.Id}}"},
        {"name": "VisitorExternalId", "statement": "{{Activity.Visitor.ExternalId}}"},
        {"name": "AssetType", "statement": "{{Activity.Asset.Type}}"},
        {"name": "AssetId", "statement": "{{Activity.Asset.Id}}"},
        {"name": "AssetName", "statement": "{{Activity.Asset.Name}}"},
        {"name": "RawData", "statement": "{{Activity.Field(RawData)}}"},
        {"name": "CampaignId", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "ExternalId", "statement": "{{Activity.ExternalId}}"}
    ],
    "External": [
        {"name": "C_EmailAddress",
         "statement": "{{Activity.Contact.Field(C_EmailAddress)}}"},
        {"name": "CampaignID", "statement": "{{Activity.Campaign.Id}}"},
        {"name": "AssetName", "statement": "{{Activity.Asset.Name}}"},
        {"name": "AssetType", "statement": "{{Activity.Asset.Type}}"},
        {"name": "AssetDate", "statement": "{{Activity.CreatedAt}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"}
    ],
    "CommonFields": [
        {"name": "ActivityId", "statement": "{{Activity.Id}}"},
        {"name": "ActivityType", "statement": "{{Activity.Type}}"},
        {"name": "ActivityDate", "statement": "{{Activity.CreatedAt}}"}
    ]
}
